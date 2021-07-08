# discord-snowflake

discordの各IDを、datetime型に変換するライブラリ。
d.pyを使うほどではないけれどIDから時間を知りたいときに

## DEMO

```py
import discosnow as ds

if __name__ == "__main__":
    message_id = 862620603979005962

    print(ds.snowflake2time(message_id))
```

## Requirement

* datetime

## Usage

```bash
https://github.com/being24/discord-snowflake
cd examples
python demo.py
```

## License

"discord-snowflake" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
