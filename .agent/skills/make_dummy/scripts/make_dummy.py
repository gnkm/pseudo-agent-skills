"""
ダミーデータを作る。

Example:

ダミーの人名を 10 個生成する。
uv run python .agent/skills/make_dummy/scripts/make_dummy.py name 10

ダミーの文章を 10 個生成する。
uv run python .agent/skills/make_dummy/scripts/make_dummy.py sentence 10
"""

import typer
from faker import Faker

fake = Faker("ja_JP")

app = typer.Typer()


@app.command()
def name(count: int):
    """
    ダミーの人名を生成する。
    """
    for _ in range(count):
        print(fake.name())


@app.command()
def sentence(count: int):
    """
    ダミーの文章を生成する。
    """
    for _ in range(count):
        print(fake.sentence())


if __name__ == "__main__":
    app()
