const Welcome = () => {
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
          <div className="text-3xl row-start-4 text-bold text-amber-600">
            Login | Sign up
          </div>
        </div>
      </div>
    </>
  );
};

export default Welcome;
