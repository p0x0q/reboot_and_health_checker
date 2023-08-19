# reboot_and_health_checker

スクリプト実行時にLoadAverageの値が高い場合に自動再起動するシェルスクリプト

# 使い方

## python3

```
[ -d "reboot_and_health_checker" ] && echo 1 || git clone https://github.com/p0x0q/reboot_and_health_checker.git && python3 reboot_and_health_checker/reboot_and_health_checker.py --la 12
```

## 最新のものを入れなおす場合

```
rm -Rf ./reboot_and_health_checker && git clone https://github.com/p0x0q/reboot_and_health_checker.git && python3 reboot_and_health_checker/reboot_and_health_checker.py --la 12
```

## CronJobに登録する(Ubuntu)
```
crontab -e

* * * * * [ -d "reboot_and_health_checker" ] && echo 1 || git clone https://github.com/p0x0q/reboot_and_health_checker.git && python3 reboot_and_health_checker/reboot_and_health_checker.py --la 12
```
