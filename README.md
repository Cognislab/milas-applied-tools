# MiLAS Applied Tools / MiLAS応用ツール

MiLAS Applied Tools は、MiLAS（Mind-Layer Architecture System）の考え方を、AI利用・AIエージェント設計・Human-AI Interaction で起きる具体的な問題に小さく適用するための試作ツール群です。

This repository provides experimental applied tools based on MiLAS for classifying AI output instability, checking AI interaction states, preventing policy-layer delegation in human-AI interaction, and related design issues.

## Start Here / 初めての方へ

MiLAS Applied Tools は、MiLAS全体を説明する場所ではありません。  
MiLASの一部の概念を、実務上のチェックリスト・分類表・レビュー補助線として試作するための作業場です。

まず理論全体を読む必要はありません。  
次のような問題に近いものから見てください。

- AIの回答が毎回ぶれる、勝手に話を広げる  
  → [出力不安定性のMiLAS分類表 v0.1](tools/milas-output-instability-classification-v0.1.md)

- 長い会話や複雑な作業で、AIの処理状態が怪しくなってきた  
  → [AI状態診断プロンプト（MiLAS版）v0.1](tools/milas-ai-state-check-prompt-v0.1.md)

- AIエージェントのtool callや更新ループを一時停止したい  
  → [NIM-Breaker v0.1](tools/nim-breaker-v0.1.md)

- AIに相談しているうちに、人間側の目的・優先順位・拒否権・停止条件がAIへ移っていないか確認したい  
  → [Human-L3-in-control spec v0.1](tools/human-l3-in-control-spec-v0.1.md)

## Status / 状態

This repository is experimental.

本リポジトリは、完成された標準規格ではありません。  
MiLASの概念を、実務上のチェックリストや分類表へ変換するための試作置き場です。

These tools do not prove the empirical validity of MiLAS.  
They are practical working tables for translating MiLAS concepts into applied design and review tools.

本ツール群は、MiLASの実証的妥当性を示すものではありません。  
MiLASの概念を、実務上の分類表・チェックリスト・レビュー表へ変換するための試作資料です。

## Available Tools / 公開中のツール

- [出力不安定性のMiLAS分類表 v0.1](tools/milas-output-instability-classification-v0.1.md)
- [AI状態診断プロンプト（MiLAS版）v0.1](tools/milas-ai-state-check-prompt-v0.1.md)
- [NIM-Breaker v0.1](tools/nim-breaker-v0.1.md)
- [Human-L3-in-control spec v0.1](tools/human-l3-in-control-spec-v0.1.md)

## Tool Overview / ツール概要

### 出力不安定性のMiLAS分類表 v0.1

AI出力のぶれ、話題逸脱、過剰補完、境界崩れなどを、MiLASの観点から整理するための分類表です。

### AI状態診断プロンプト（MiLAS版）v0.1

長い会話や複雑なタスクで、AIの処理状態が不安定になっていないかを確認するための軽量プロンプトです。

### NIM-Breaker v0.1

AIエージェントやtool callの更新ループを一時停止し、追加処理を抑制するための実験的な停止補助ツールです。

### Human-L3-in-control spec v0.1

Human-in-the-loop does not necessarily mean human control.  
人間がループ内にいても、人間側の目的・優先順位・拒否権・停止条件が保たれているとは限りません。

Human-L3-in-control は、Human-AI Interaction において、人間側の方針層がAIへ暗黙に委譲されていないかを確認するための軽量チェックリストです。

## Planned Tools / 今後の候補

- プロンプト／スキーマ／ツール権限の境界設計表
- AIエージェント設計レビュー表
- RAG崩れ診断表
- Control-as-Load Check / Control Pressure Management checklist

## Development Policy / 開発方針

- Each tool should be small and usable.
- Each tool should be treated as experimental.
- MiLAS concepts should be translated into practical tables, checklists, or review forms.
- These tools should not be presented as validated standards.

---

- 各ツールは小さく、使える形にする。
- 各ツールは実験的な試作として扱う。
- MiLAS概念は、分類表・チェックリスト・レビュー表などの実務形式に翻訳する。
- 本ツール群を、検証済み標準や診断ツールとして提示しない。

## Notes / 注意

MiLAS Applied Tools は、MiLAS本体の完全な説明ではありません。  
また、心理診断、臨床的評価、安全認証、正式なAIガバナンス手法の代替でもありません。

This repository does not provide psychological diagnosis, clinical assessment, safety certification, or a substitute for formal AI governance frameworks.

## License / ライセンス

License: MIT License

Note: This license applies to the files in this repository.  
The MiLAS name, conceptual framework, and related publications remain attributed to Mameta Edanari / Cognis-Lab.

## Author / 著者

Mameta Edanari / 枝成豆太  
Cognis-Lab
