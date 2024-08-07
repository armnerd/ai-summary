import json
import os
import pickle
import argparse

try:
    import tiktoken
    #from langchain_community.embeddings import HuggingFaceEmbeddings

    # 升级替换告警-Jesse
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS
except ImportError:
    raise ImportError("Please install lang chain-community first.")


class DocumentRetriever:
    def __init__(self, index_folder):
        self.index_folder = index_folder
        self.vectorstore = None
        self.chunk_id_to_index = None
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self._init()
        self.enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

    def _init(self):
        self.vectorstore = FAISS.load_local(
            folder_path=self.index_folder,
            embeddings=self.embeddings,
            # 修复M1下报错-Jesse
            allow_dangerous_deserialization=True,
        )
        with open(os.path.join(self.index_folder, "chunk_id_to_index.pkl"), "rb") as f:
            self.chunk_id_to_index = pickle.load(f)

    def __call__(self, query: str, size: int = 5, target_length: int = 256):
        if self.vectorstore is None:
            raise Exception("Vectorstore not initialized")

        result = self.vectorstore.similarity_search(query=query, k=size)
        expanded_chunks = self.do_expand(result, target_length)

        return json.dumps(expanded_chunks, indent=4)

    def do_expand(self, result, target_length):
        expanded_chunks = []
        # do expansion
        for r in result:
            source = r.metadata["source"]
            chunk_id = r.metadata["chunk_id"]
            content = r.page_content

            expanded_result = content
            left_chunk_id, right_chunk_id = chunk_id - 1, chunk_id + 1
            left_valid, right_valid = True, True
            chunk_ids = [chunk_id]
            while True:
                current_length = len(self.enc.encode(expanded_result))
                if f"{source}_{left_chunk_id}" in self.chunk_id_to_index:
                    chunk_ids.append(left_chunk_id)
                    left_chunk_index = self.vectorstore.index_to_docstore_id[
                        self.chunk_id_to_index[f"{source}_{left_chunk_id}"]
                    ]
                    left_chunk = self.vectorstore.docstore.search(left_chunk_index)
                    encoded_left_chunk = self.enc.encode(left_chunk.page_content)
                    if len(encoded_left_chunk) + current_length < target_length:
                        expanded_result = left_chunk.page_content + expanded_result
                        left_chunk_id -= 1
                        current_length += len(encoded_left_chunk)
                    else:
                        expanded_result += self.enc.decode(
                            encoded_left_chunk[-(target_length - current_length):],
                        )
                        current_length = target_length
                        break
                else:
                    left_valid = False

                if f"{source}_{right_chunk_id}" in self.chunk_id_to_index:
                    chunk_ids.append(right_chunk_id)
                    right_chunk_index = self.vectorstore.index_to_docstore_id[
                        self.chunk_id_to_index[f"{source}_{right_chunk_id}"]
                    ]
                    right_chunk = self.vectorstore.docstore.search(right_chunk_index)
                    encoded_right_chunk = self.enc.encode(right_chunk.page_content)
                    if len(encoded_right_chunk) + current_length < target_length:
                        expanded_result += right_chunk.page_content
                        right_chunk_id += 1
                        current_length += len(encoded_right_chunk)
                    else:
                        expanded_result += self.enc.decode(
                            encoded_right_chunk[: target_length - current_length],
                        )
                        current_length = target_length
                        break
                else:
                    right_valid = False

                if not left_valid and not right_valid:
                    break

            expanded_chunks.append(
                {
                    "chunk": expanded_result,
                    "metadata": r.metadata,
                    # "length": current_length,
                    # "chunk_ids": chunk_ids
                },
            )
        return expanded_chunks


def search_knowledge(data):
    """
    根据输入的data搜索本地数据中的信息
    Parameters:
    data (str): 搜索关键词.
    """
    if not data:
        print("Error: No query provided.")
        exit(1)

    # Initialize with the path to your index folder
    index_folder = "/Users/zane/projects/rag/knowledge"
    retriever = DocumentRetriever(index_folder)

    # Use the query from the command line arguments
    query = data
    size = 5  # Number of results to retrieve
    target_length = 256  # Target length of expanded content

    # Retrieve documents based on the query
    results = retriever(query, size, target_length)
    # Print the results
    print(results)
    return results


# Example usage
if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='what is fix?')
    parser.add_argument(
        '--query',
        nargs='?',
        type=str,
        help='The query to retrieve documents for.',
        default="what is algebra",
    )
    args = parser.parse_args()

    # Check if query was provided
    if not args.query:
        parser.print_help()
        print("Error: No query provided.")
        exit(1)

    # Initialize with the path to your index folder
    index_folder = "knowledge"
    retriever = DocumentRetriever(index_folder)

    # Use the query from the command line arguments
    query = args.query
    size = 5  # Number of results to retrieve
    target_length = 256  # Target length of expanded content

    # Retrieve documents based on the query
    results = retriever(query, size, target_length)

    # Print the results
    print(results)
