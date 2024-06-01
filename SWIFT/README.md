# SWIFT (Scalable lightWeight Infrastructure for Fine-Tuning)
## 📖 目录
- [简介](#-简介)
- [新闻](#-新闻)
- [安装](#%EF%B8%8F-安装)
- [快速开始](#-快速开始)
- [文档](#-文档)

## 📝 简介
SWIFT支持近**200种LLM和MLLM**（多模态大模型）的训练、推理、评测和部署。开发者可以直接将SWIFT框架应用到自己的Research和生产环境中，实现模型训练评测到应用的完整链路。除支持了[PEFT](https://github.com/huggingface/peft)提供的轻量训练方案外，SWIFT也提供了一个完整的Adapters库以支持最新的训练技术，如NEFTune、LoRA+、LLaMA-PRO等，这个适配器库可以脱离训练脚本直接使用在自己的自定流程中。同时，SWIFT也在拓展其他模态的能力，目前SWIFT支持了AnimateDiff的全参数训练和LoRA训练。

现在我们项目使用本项目自定义[数据集](https://github.com/SmartFlowAI/EmoLLM/blob/main/datasets)，并将其转化成合适的json格式（见SWIFT代码部分），使用SWIFT进行微调（现在项目已完成对Qwen-7b的微调）。

SWIFT具有丰富的文档体系，如有使用问题请请查看[这里](https://github.com/modelscope/swift/tree/main/docs/source/LLM).

大家可以在[Huggingface space](https://huggingface.co/spaces/tastelikefeet/swift) 和 [ModelScope创空间](https://www.modelscope.cn/studios/iic/Scalable-lightWeight-Infrastructure-for-Fine-Tuning/summary) 中体验SWIFT web-ui功能。

## 🎉 新闻
- 🔥2024.04.26: 完成对qwen-7b-chat模型的SWIFT微调，并且上传到[Modelscope](https://www.modelscope.cn/models/monbear/qwen-7b-chat-lora/summary).
- 🔥2024.04.27: 完成对qwen-7b-chat微调模型的量化，并且上传到[Modelscope](https://www.modelscope.cn/models/monbear/qwen1half-7b-chat-lora/summary).
- 🔥2024.04.29: 获得[AI 赋能大学计划“全国高校行”](https://mp.weixin.qq.com/s/yyaulQ1wBzKq5cXaGl2Wag)一等奖

## 🛠️ 安装

SWIFT在Python环境中运行。请确保您的Python版本高于3.8。
