"use client";
import TraceTerminal from "./TraceTerminal";

export default function ExecutionPanel() {
  return (
    <div className="w-96 p-4 bg-white shadow rounded">
      <h2 className="font-bold text-xl mb-4">Execution Trace</h2>
      <TraceTerminal />
    </div>
  );
}

