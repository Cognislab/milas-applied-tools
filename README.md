# MiLAS Applied Tools / MiLAS応用ツール

MiLAS Applied Tools は、MiLAS（Mind-Layer Architecture System）の考え方を、AI出力の不安定性、エージェント設計、Human-in-the-loop条件、RAG崩れなどの実務的問題に適用するための試作ツール群です。

This repository provides experimental applied tools based on MiLAS for classifying AI output instability and related design issues.

## 初めての方へ / Start Here

MiLAS Applied Tools は、MiLAS（Mind-Layer Architecture System）の考え方を、AI利用やAIエージェント設計で起きる具体的な問題に小さく適用するための試作ツール集です。

まず理論全体を読む必要はありません。  
次のような問題に近いものから見てください。

- AIの回答が毎回ぶれる、勝手に話を広げる  
  → [出力不安定性のMiLAS分類表 v0.1](tools/milas-output-instability-classification-v0.1.md)

- 長い会話や複雑な作業で、AIの処理状態が怪しくなってきた  
  → [AI状態診断プロンプト（MiLAS版）v0.1](tools/milas-ai-state-check-prompt-v0.1.md)

- AIエージェントのtool callや更新ループを一時停止したい  
  → [NIM-Breaker v0.1](tools/nim-breaker-v0.1.md)

これらのツールは、MiLASの妥当性を証明するものではありません。  
AI出力やエージェント挙動の不安定性を、入力・解釈・境界・制御・運用の観点から整理するための実験的な補助線です。

## Status / 状態

This repository is experimental.

本リポジトリは、完成された標準規格ではありません。  
MiLASの概念を、実務上のチェックリストや分類表へ変換するための作業場です。

## Available Tools / 公開中のツール

## Available Tools / 公開中のツール

- [出力不安定性のMiLAS分類表 v0.1](tools/milas-output-instability-classification-v0.1.md)
- [AI状態診断プロンプト（MiLAS版）v0.1](tools/milas-ai-state-check-prompt-v0.1.md)
- [NIM-Breaker v0.1](tools/nim-breaker-v0.1.md)

## Planned Tools / 今後の候補

- Human-in-the-loop移行条件チェックリスト
- プロンプト／スキーマ／ツール権限の境界設計表
- AIエージェント設計レビュー表
- RAG崩れ診断表

## Notes / 注意

These tools do not prove the empirical validity of MiLAS.  
They are practical working tables for translating MiLAS concepts into applied design and review tools.

本ツール群は、MiLASの実証的妥当性を示すものではありません。  
MiLASの概念を、実務上の分類表・チェックリスト・レビュー表へ変換するための試作資料です。

License: MIT License

Note:
This license applies to the files in this repository.
The MiLAS name, conceptual framework, and related publications remain attributed to Mameta Edanari / Cognis-Lab.

## Author / 著者

Mameta Edanari / 枝成豆太  
Cognis-Lab
