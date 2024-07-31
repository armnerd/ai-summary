# Mac Resource

## 1.如何修改主机名?

```bash
1.设置显示

vim /etc/zshrc
#-------------------------
PS1="[jesse@%m %1~ %#]# "
#-------------------------

2.主机名修改
sudo scutil --set HostName XXX
```

## 2.Homebrew install

```bash
2.1 国内镜像安装:
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```



