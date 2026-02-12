"use client";
import ReactFlow, { Background } from "reactflow";
import "reactflow/dist/style.css";

export default function Canvas() {
  return (
    <div className="flex‑1 border rounded shadow p-2 bg‑white">
      <h2 className="font-bold text-lg mb-2">Agent Canvas</h2>
      <ReactFlow nodes={[]} edges={[]}>
        <Background />
      </ReactFlow>
    </div>
  );
}

