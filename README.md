# TalkWithPLaMo

株式会社Preferred Elementsが開発する大規模言語モデルPLaMo™（プラモ）β版を使って対話するPythonプログラムです。  
PLaMoを対話エンジンとして使用するコミュニケーションロボットを試作するにあたり、system rollの設定内容を試行錯誤するために作成しました。  
(2024年8月16日時点では、PLaMoを好きなキャラクターに仕立て上げることができず断念しました。)

過去19回分の対話内容をmessagesとして投げます。

## 導入
OpenAI Python libralyとpython-dotenvを使用します。それぞれ導入してください。

```
pip install openai
pip install python-dotenv
```

URLとAPIキーをpython-dotenvを使って読み込みます。  
plamotest.py と同じディレクトリに .envファイルを作り、以下の内容を設定してください。  
```
API_HOST=https://platform.preferredai.jp
API_KEY=your api key
```
APIキーはPLaMoのページから取得してください。

plamotest.py を実行し、会話を楽しんでください。  
以下の行を変更し、様々なsystem rollを試すことができます。

```
sysmess = {"role": "system", "content": "あなたの名前は山田太郎です。"}
```