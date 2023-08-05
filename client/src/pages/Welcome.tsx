import { useRef } from "react";
import Credentials from "../components/credentials";

const Welcome = () => {
  const targetRef = useRef<HTMLDivElement | null>(null);

  return (
    <>
      <div className="bg-orange-200">
        <div className="grid grid-rows-4 place-items-center h-screen">
          <img className="row-start-1" src="logo.png"></img>
          <div className="flex flex-col items-center text-9xl font-radley row-start-2">
            <div>Welcome to</div>
            <div className="italic text-amber-600">libTrack</div>
          </div>
          <div className="text-5xl row-start-3">
            Track and store your books online
          </div>
          <a
            href=""
            className="text-3xl row-start-4 text-bold text-amber-600"
            onClick={(event) => {
              event.preventDefault();
              targetRef.current?.scrollIntoView({ behavior: "smooth" });
            }}
          >
            Log in | Sign up
          </a>
        </div>
        <div ref={targetRef} className="flex">
          <div className="w-1/2 h-screen bg-amber-600 grid grid-rows-6 place-items-center">
            <div className="text-4xl font-radley row-start-1">
              Returning user?
            </div>
            <div className="text-8xl font-radley row-start-2">Log in</div>

            <Credentials />

            <button className="bg-amber-700 rounded-full row-start-6 px-9 py-5 hover:bg-amber-800">
              <div className="font-radley text-6xl">Log in</div>
            </button>
          </div>

          <div className="w-1/2 h-screen bg-amber-700 grid grid-rows-6 place-items-center"></div>
        </div>
      </div>
    </>
  );
};

export default Welcome;
