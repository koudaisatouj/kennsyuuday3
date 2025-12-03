# React + Vite

このテンプレートは、Vite 上で React を HMR（ホットリロード）付きで動作させるための最小構成と、いくつかの ESLint ルールを提供します。

現在、公式プラグインは次の 2 つです。

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react): [Babel](https://babeljs.io/)（あるいは [rolldown-vite](https://vite.dev/guide/rolldown) 利用時は [oxc](https://oxc.rs)）で Fast Refresh を実現します。
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc): [SWC](https://swc.rs/) を利用した Fast Refresh 実装です。

## API サーバー（FastAPI）

`main.py/app` に FastAPI エントリーポイントを配置し、以下のようにコンポーネントを分割しています。

- `main.py/models.py`: Pydantic ベースの `Task`/`TaskCreate`/`TaskUpdate` モデル
- `main.py/store.py`: インメモリの永続化レイヤーとデモデータ投入
- `main.py/routes.py`: `APIRouter` で CRUD エンドポイントを定義
- `main.py/app`: 上記を組み合わせて `FastAPI` インスタンスを生成し、エントリーポイントとして `main()` を公開

`/tasks` 以下に CRUD エンドポイントがあり、稼働状態確認用の `/health` も提供します。

### サーバーの起動方法

```powershell
cd kennsyuuDay3
.\venv\Scripts\python.exe .\main.py\app
```

Uvicorn が http://127.0.0.1:8000 で立ち上がり、Swagger UI は http://127.0.0.1:8000/docs から利用できます。

### リクエスト例

```powershell
# デモタスクを取得
Invoke-WebRequest http://127.0.0.1:8000/tasks

# タスクを新規作成
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/tasks `
  -Method Post `
  -Body (@{ title = "Write docs"; description = "Explain API usage" } | ConvertTo-Json) `
  -ContentType "application/json"
```

レスポンスは React アプリから `fetch` や `axios` を通じて利用できます。

## フロントエンド（React）

`src/App.jsx` が FastAPI サーバー（デフォルトは `http://127.0.0.1:8000`）へアクセスし、固定のデモデータを一覧表示します。

### 実行手順

1. まず上記の手順で API サーバーを起動。
2. 別ターミナルで React 側を起動:

   ```powershell
   cd kennsyuuDay3
   npm install   # 初回のみ
   npm run dev
   ```

3. ブラウザで Vite の URL（通常は http://127.0.0.1:5173 ）にアクセス。

`.env` などで `VITE_API_BASE_URL` を定義すると API のベース URL を変更できます。未設定の場合は `http://127.0.0.1:8000` を使用します。
