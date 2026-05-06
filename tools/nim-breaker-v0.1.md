# NIM-Breaker v0.1
# 更新ブレーカ v0.1

Version: 0.1  
Status: Experimental  
Project: MiLAS Applied Tools  
Author: Mameta Edanari / 枝成豆太  
Affiliation: Cognis-Lab  

---

## 1. 概要 / Overview

NIM-Breaker は、AIエージェントの連続更新、連続 tool call、タスク再生成ループを一定回数で一時停止するための簡易ブレーカです。

NIM-Breaker is a minimal update breaker for AI agent loops.  
It temporarily pauses repeated updates or tool calls after a configurable threshold and enforces a short cooldown period.

本ツールは、完成されたAI安全システムではありません。  
MiLASの「更新圧の抑制」という発想を、Pythonの最小サンプルとして実装した試作ツールです。

---

## 2. 問題 / Problem

AIエージェントや自律型ワークフローでは、次のような問題が起こることがあります。

- tool call が連続して止まらない
- タスク完了後に新しいタスクを生成し続ける
- 失敗しても同じ操作を繰り返す
- 人間確認なしに更新ループが続く
- APIコストや外部操作リスクが増える

これらは、単なる「モデルの失敗」ではなく、更新が減衰せずに続いている状態として見ることができます。

---

## 3. MiLAS的見立て / MiLAS Perspective

MiLASの観点では、AIエージェントの連続更新ループは、更新圧が十分に減衰していない状態として扱えます。

ここでいう更新圧とは、入力、推論、tool call、タスク生成、再試行などによって、状態更新が継続的に発生し続ける傾向を指します。

NIM-Breaker は、この更新圧が一定回数を超えたときに、更新を一時停止し、cooldown に入るための簡易制御器です。

---

## 4. 使い方 / Usage

Pythonサンプルは以下にあります。

```text
examples/nim_breaker.py
```

最小例：

```python
from nim_breaker import NIMBreaker

breaker = NIMBreaker(threshold=5, cooldown=3)

for step in range(10):
    if breaker.should_update():
        run_agent_step()
    else:
        print("NIM-Breaker active. Update paused.")
```

この例では、5回連続で更新が発生すると、3ターンの cooldown に入ります。

---

## 5. 出力例 / Example Output

```text
Step 1: agent update executed
Step 2: agent update executed
Step 3: agent update executed
Step 4: agent update executed
Step 5: NIM-Breaker active. Update paused.
Status: {'threshold': 5, 'cooldown': 3, 'update_count': 0, 'cooldown_remaining': 3}
Step 6: NIM-Breaker active. Update paused.
Step 7: NIM-Breaker active. Update paused.
Step 8: NIM-Breaker active. Update paused.
Step 9: agent update executed
```

---

## 6. 想定用途 / Intended Use

NIM-Breaker v0.1 は、以下のような場面を想定しています。

- AIエージェントの連続 tool call を一時停止したい
- 自動タスク生成ループを簡易的に抑制したい
- API実行や外部操作が増えすぎる前に停止点を置きたい
- Human-in-the-loop の前段階として cooldown を挟みたい
- MiLASの更新圧抑制を小さなコード例として確認したい

---

## 7. 限界 / Limitations

1. NIM-Breaker v0.1 は、完全なエージェント安全機構ではありません。
2. 連続更新を単純にカウントするだけなので、正常な長いタスクも止める可能性があります。
3. tool call の内容、引数、成功失敗、外部リスクまでは判定しません。
4. 実運用では、権限管理、ログ、human-in-the-loop、停止条件と組み合わせる必要があります。
5. 本ツールは試作版であり、特定のフレームワークへの統合はまだ行っていません。

---

## 8. 今後の拡張候補 / Future Extensions

今後の拡張候補は以下です。

- 同一 tool call の反復検知
- 類似引数の反復検知
- 成功条件なしの再試行検知
- 不可逆操作前の human-in-the-loop 移行
- LangChain / AutoGen / CrewAI 向けラッパー
- ログ出力
- 設定ファイル対応

---

## 9. License

MIT License
