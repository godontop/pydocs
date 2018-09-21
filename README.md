# docs
个人笔记

* [tmux](#tmux)

# tmux
OS： CentOS Linux release 7.5.1804 (Core)  
package： tmux  
pathname： /usr/bin/tmux

## 选项
tmux的外观和特性可以通过改变各种选项的值来进行修改。有三种选项：`服务器选项`，`会话选项`和`窗口选项`。

**tmux** 服务器有一组不适用于任何特定的窗口或会话的全局选项。这些选项通过 **set-option -s** 命令修改，或者通过 **show-options -s** 命令显示。

    设置选项的命令如下：

    set-option [-agoqsuw] [-t target-session | target-window] option value
                (alias: set)
		    设置窗口选项用 **-w** (等同于 **set-window-option** 命令)，服务器选项用 **-s**，否则为一个会话选项。

		    如果 **-g** 被指定，则全局会话或窗口选项被设置。

		    可用的会话选项是：

		    history-limit <u>lines</u>
		            设置窗口历史中要保留的最大行数。这个设置仅用于新窗口 - 已存在的窗口历史大小不作调整并保持它们被创建时的限制。

    show-options [-gqsvw] [-t target-session | target-window] [option]
                  (alias: show)
            如果 -g 被使用，则列出全局会话或窗口选项。

## 文件
     ~/.tmux.conf       **tmux** 默认配置文件。
     /etc/tmux.conf     系统级配置文件。

~/.tmux.conf  
```
set -g history-limit 3000 
```

## 常见用法
tmux show -g  
列出全局会话或窗口选项

## 备注
1. `~/.tmux.conf` 文件需要手工创建，系统本身不带。