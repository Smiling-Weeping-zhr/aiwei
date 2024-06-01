# SWIFT (Scalable lightWeight Infrastructure for Fine-Tuning)
## 📖 Table of Contents
- [Introduction](#-introduction)
- [News](#-news)
- [Installation](#%EF%B8%8F-installation)
- [Getting Started](#-getting-started)
- [Documentation](#-documentation)

## 📝 Introduction
SWIFT supports the training, inference, evaluation and deployment of nearly 200 LLMs and MLLMs (multimodal large models). Developers can directly apply the SWIFT framework to their own research and production environment, and realize the complete link from model training and evaluation to application. In addition to supporting the lightweight training solutions provided by [PEFT](https://github.com/huggingface/peft), SWIFT also provides a complete library of adapters to support the latest training technologies, such as NEFTune, LoRA+, LLaMA-PRO, etc., which can be used directly in your own custom workflows without training scripts. At the same time, SWIFT is also expanding the capabilities of other modalities, and currently supports AnimateDiff full-parameter training and LoRA training.

Now our project uses this project to customize the [dataset](https://github.com/SmartFlowAI/EmoLLM/blob/main/datasets) and convert it to a suitable json format (see the SWIFT code section), and fine-tune it in SWIFT (the project has now finished fine-tuning Qwen-7b-chat).

SWIFT has a rich documentation system, if you have any questions about using it, please check [here](https://github.com/modelscope/swift/tree/main/docs/source/LLM).

You can find it in the [Huggingface space](https://huggingface.co/spaces/tastelikefeet/swift) and [ModelScope]( https://www.modelscope.cn/studios/iic/Scalable-lightWeight-Infrastructure-for-Fine-Tuning/summary) to experience SWIFT web-ui functionality.

## 🎉 News
- 🔥2024.04.26: Complete the SWIFT fine-tuning of the qwen-7b-chat model and upload it to [ModelScope](https://www.modelscope.cn/models/monbear/qwen-7b-chat-lora/summary).
- 🔥2024.04.27: Complete the quantization of the qwen-7b-chat fine-tuning model and upload it to [ModelScope](https://www.modelscope.cn/models/monbear/qwen1half-7b-chat-lora/summary).
- 🔥2024.04.29: obtain[AI 赋能大学计划“全国高校行”](https://mp.weixin.qq.com/s/yyaulQ1wBzKq5cXaGl2Wag) First prize

## 🛠️ Installation

SWIFT runs in a Python environment. Please make sure your Python version is higher than 3.8.
