---
name: make_dummy
description: ダミーデータを生成する。ダミーデータを生成するときに使う。
---

以下の手順でダミーデータを生成します。

## 人名の場合

`make_dummy.py` に `name` 引数を渡すと、人名を生成します。
第二引数に生成する人数を指定します。

```
uv run python .agent/skills/make_dummy/scripts/make_dummy.py name 10
```

## ダミーテキストの場合

`make_dummy.py` に `sentence` 引数を渡すと、ダミーテキストを生成します。
第二引数に生成する文章の数を指定します。

```
uv run python .agent/skills/make_dummy/scripts/make_dummy.py sentence 10
```
