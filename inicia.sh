#!/data/data/com.termux/files/usr/bin/bash

DB="$HOME/.filebrowser/filebrowser.db"
PORT=8080

IP=$(python -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
print(s.getsockname()[0])
s.close()
")

echo "======================================"
echo "       INICIANDO FILE BROWSER"
echo "======================================"
echo

filebrowser \
    -a 0.0.0.0 \
    -p "$PORT" \
    -r /storage/emulated/0 \
    -d "$DB" &

SERVER_PID=$!

sleep 2

if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    echo "Erro ao iniciar o servidor."
    exit 1
fi

echo "Servidor iniciado!"
echo
echo "Endereço: http://$IP:$PORT"
echo
echo "Pressione CTRL+C para encerrar."

wait "$SERVER_PID"
