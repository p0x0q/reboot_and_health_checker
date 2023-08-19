# reboot_and_health_checker

スクリプト実行時にLoadAverageの値が高い場合に自動再起動するシェルスクリプト

# 使い方

## shell

```
[ -d "reboot_and_health_checker" ] && echo 1 || git clone https://github.com/p0x0q/reboot_and_health_checker.git && cd reboot_and_health_checker && python3 reboot_and_health_checker.sh --la 12
```

## python3

```
[ -d "reboot_and_health_checker" ] && echo 1 || git clone https://github.com/p0x0q/reboot_and_health_checker.git && cd reboot_and_health_checker && python3 reboot_and_health_checker.py --la 12
```
