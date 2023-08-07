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

        {/* login/signup page */}
        <div ref={targetRef} className="h-screen w-screen">
          <div className="bg-amber-600 h-full w-1/2 flex flex-col items-center justify-around">
            <div className="text-4xl font-radley">Returning user?</div>
            <div className="text-8xl font-radley">Log in</div>
            <div className="bg-amber-700 w-1/3 h-1/2 rounded-3xl"></div>
            <button className="bg-amber-700 text-6xl font-radley rounded-full py-5 px-10 hover:bg-amber-800">
              Log in
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default Welcome;
