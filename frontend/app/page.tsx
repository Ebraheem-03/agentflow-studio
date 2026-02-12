import Canvas from "./components/Canvas";
import ExecutionPanel from "./components/ExecutionPanel";

export default function Home() {
  return (
    <div className="flex h-screen gap-4 bg-gray-50">
      <Canvas />
      <ExecutionPanel />
    </div>
  );
}

