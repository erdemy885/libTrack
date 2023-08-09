interface Props {
  type: "login" | "signup";
}

const AuthForm = ({ type }: Props) => {
  const isLogin = type === "login";
  return (
    <>
      <div
        className={`bg-amber-${
          isLogin ? 600 : 700
        } h-full w-1/2 flex flex-col items-center justify-around`}
      >
        <div className="text-4xl font-radley">
          {isLogin ? "Returning user?" : "New user?"}
        </div>
        <div className="text-8xl font-radley">
          {isLogin ? "Log in" : "Sign up"}
        </div>
        <div
          className={`bg-amber-${
            isLogin ? 700 : 600
          } w-1/2 h-1/2 rounded-3xl flex flex-col justify-around px-10`}
        >
          <div className="text-3xl flex flex-col">
            <span>Username</span>
            <input type="text" className="rounded-lg"></input>
          </div>
          <div className="text-3xl flex flex-col">
            <span>Password</span>
            <input type="password" className="rounded-lg"></input>
          </div>
          {!isLogin && (
            <div className="text-3xl flex flex-col">
              <span>Confirm Password</span>
              <input type="password" className="rounded-lg"></input>
            </div>
          )}
          <div className="text-2xl flex mx-2 space-x-3 align-center">
            <input type="checkbox" />
            <span>Remember me</span>
          </div>
        </div>
        <button
          className={`bg-amber-${
            isLogin ? 700 : 600
          } text-6xl font-radley rounded-full py-3 px-6 hover:bg-amber-${
            isLogin ? 800 : 500
          }`}
        >
          {isLogin ? "Log in" : "Sign up"}
        </button>
      </div>
    </>
  );
};

export default AuthForm;
