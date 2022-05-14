---
jupytext:
  notebook_metadata_filter: all
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.8.5
---

# 【課題】ビット反転ボードの操作を見つける

ビット反転ボードという架空のボードとグローバー探索を使って、ある数字を別の数字に変換する問題を考えてみます。

+++ {"pycharm": {"name": "#%% md\n"}}

## 問題設定

{doc}`グローバーのアルゴリズム <grover>`では、$N=2^6$個の要素を持つリスト（$=[0,1,2,\cdots,63]$）から45を見つける問題を考えました。ここではこの6量子ビットの探索問題をベースに考えますが、問題は以下のようなものです。

あるボードがあって、そのボードにはビット毎に0か1を書き込むことができます。例えば45であれば、2進数表記$45=101101$を6つの枠を持つボードに書き込みます。

```{image} figs/grover_kadai1.png
:alt: grover_kadai1
:width: 500px
:align: center
```

このボードは、ある桁のビットを「押す」と、そのビットと一つ隣のビットが反転するという特徴があります。例えば、45のボードの上から2桁目のビットを「押す」と、$21=010101$に変わると言った具合です。

```{image} figs/grover_kadai2.png
:alt: grover_kadai2
:width: 500px
:align: center
```

この課題では、このボードを使ってある数字（例えば45）を別の数字（例えば13）に変換するという問題を考えます。特に、最小の押し下げ回数で目的の数字が得られるにはどのビットを押し下げるのが良いか、そのビット位置を見つける問題です。

```{image} figs/grover_kadai3.png
:alt: grover_kadai3
:width: 500px
:align: center
```

+++ {"pycharm": {"name": "#%% md\n"}}

## ヒント

1. ボード上の数字を記録するレジスタを準備して、初期値45をセットします。
2. 見つけたい答えは「どのビットを押すか」なので、6ビットの数字の場合は、6量子ビットの「全ての押し下げパターンの重ね合わせ」を持つレジスタを作ると良いでしょう。
3. 各ビットの押し下げに対して、ボードのビット反転を行う操作を量子ゲートで実装することが考えられます。
4. ボード上の数字が欲しい答え13の場合に位相反転するオラクルを考えてみてください。

+++ {"pycharm": {"name": "#%% md\n"}}

**提出するもの**
- この問題を解く量子回路
- 45を13に変換するビット押し下げパターンを高確率で見つけていることが分かる結果