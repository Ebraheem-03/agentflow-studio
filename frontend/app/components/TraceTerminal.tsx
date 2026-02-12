"use client";
import { useEffect, useState } from "react";

export default function TraceTerminal() {
  const [log, setLog] = useState<string[]>([]);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/trace/demo");
    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setLog((prev) => [...prev, JSON.stringify(data)]);
    };
  }, []);

  return (
    <pre className="h-80 bg-gray-900 text-green-300 p-2 overflow-auto text-sm">
      {log.map((l, i) => (
        <div key={i}>{l}</div>
      ))}
    </pre>
  );
}

