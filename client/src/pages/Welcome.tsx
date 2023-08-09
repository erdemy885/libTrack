import { useRef } from "react";
import AuthForm from "../components/AuthForm";

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
          <span className="text-5xl">Track store your books online</span>
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

        {/* login/signup screen */}
        <div ref={targetRef} className="h-screen flex">
          <AuthForm type="login" />
          <AuthForm type="signup" />
        </div>
      </div>
    </>
  );
};

export default Welcome;
