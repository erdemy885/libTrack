import { useRef } from "react";
import Credentials from "../components/credentials";

const Welcome = () => {
  const targetRef = useRef<HTMLDivElement | null>(null);

  return (
    <>
      <div className="bg-orange-200">
        <div className="flex flex-col justify-around items-center h-screen">
          <img src="logo.png"></img>
          <div className="flex flex-col items-center text-9xl font-radley">
            <span>Welcome to</span>
            <span className="italic text-amber-600">libTrack</span>
          </div>
          <span className="text-5xl">Track and store your books online</span>
          <a
            href=""
            className="text-3xl text-bold text-amber-600"
            onClick={(event) => {
              event.preventDefault();
              targetRef.current?.scrollIntoView({ behavior: "smooth" });
            }}
          >
            Log in | Sign up
          </a>
        </div>

        {/* login/signup page */}
        <div ref={targetRef} className="h-screen flex">
          {/* login */}
          <div className="bg-amber-600 h-full w-1/2 flex flex-col items-center justify-around">
            <div className="text-4xl font-radley">Returning user?</div>
            <div className="text-8xl font-radley">Log in</div>
            <div className="bg-amber-700 w-1/2 h-1/2 rounded-3xl flex flex-col justify-around px-10">
              <div className="text-3xl flex flex-col">
                <span>Username</span>
                <input type="text" className="rounded-lg"></input>
              </div>
              <div className="text-3xl flex flex-col">
                <span>Password</span>
                <input type="password" className="rounded-lg"></input>
              </div>
              <div className="text-3xl flex flex-col">
                <span>Confirm Password</span>
                <input type="password" className="rounded-lg"></input>
              </div>
              <div className="text-2xl flex mx-2 space-x-3 align-center">
                <input type="checkbox"></input>
                <span>Remember me</span>
              </div>
            </div>
            <button className="bg-amber-700 text-6xl font-radley rounded-full py-3 px-6 hover:bg-amber-800">
              Log in
            </button>
          </div>

          {/* signup */}
          <div className="bg-amber-700 h-full w-1/2 flex flex-col items-center justify-around">
            <div className="text-4xl font-radley">New user?</div>
            <div className="text-8xl font-radley">Sign up</div>
            <div className="bg-amber-600 w-1/2 h-1/2 rounded-3xl flex flex-col justify-around px-10">
              <div className="text-3xl flex flex-col">
                <span>Username</span>
                <input type="text" className="rounded-lg"></input>
              </div>
              <div className="text-3xl flex flex-col">
                <span>Password</span>
                <input type="password" className="rounded-lg"></input>
              </div>
              <div className="text-3xl flex flex-col">
                <span>Confirm Password</span>
                <input type="password" className="rounded-lg"></input>
              </div>
              <div className="text-2xl flex mx-3 space-x-3 align-center">
                <input type="checkbox"></input>
                <span>Remember me</span>
              </div>
            </div>
            <button className="bg-amber-600 text-6xl font-radley rounded-full py-3 px-6 hover:bg-amber-500">
              Sign up
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default Welcome;
