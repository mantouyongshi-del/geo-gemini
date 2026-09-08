#!/bin/bash

# ==============================================================================
# GEO-Matrix AI 搜索引擎优化与巡检系统 一键启动脚本
# ==============================================================================

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "🚀 正在启动 GEO-Matrix 商业系统..."
echo "项目根目录: $ROOT_DIR"

# 1. 启动后端 FastAPI (端口 8000)
echo "📡 正在启动后端 FastAPI 业务服务 (端口 8000)..."
cd "$ROOT_DIR/backend"
./venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 > backend.log 2>&1 &
BACKEND_PID=$!
echo "✓ 后端服务已在后台运行 (PID: $BACKEND_PID)"

# 2. 启动前端 Vite (端口 5173)
echo "💻 正在启动前端可视化看板 (端口 5173)..."
cd "$ROOT_DIR/frontend"
npm run dev -- --host 0.0.0.0 --port 5173 > frontend.log 2>&1 &
FRONTEND_PID=$!
echo "✓ 前端服务已在后台运行 (PID: $FRONTEND_PID)"

sleep 2

TOKEN=$(cd "$ROOT_DIR" && ./backend/venv/bin/python3 -c "
from backend.app.core.security import generate_share_token
print(generate_share_token(1))
")

echo ""
echo "=================================================================="
echo "🎉 GEO 商业全栈系统已就绪！"
echo "=================================================================="
echo "👉 客户报表访问链接: http://localhost:5173/#/ai_report?code=$TOKEN"
echo "👉 后端 API 文档:     http://localhost:8000/api/v1/docs"
echo "👉 后端运行日志:     $ROOT_DIR/backend/backend.log"
echo "👉 前端运行日志:     $ROOT_DIR/frontend/frontend.log"
echo "=================================================================="
echo "按 Ctrl+C 可停止运行..."

trap "kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT SIGTERM
wait
