const Credentials = () => {
  return (
    <>
      <div className="w-1/2 h-96 bg-amber-700 rounded-3xl place-items-center grid grid-rows-4">
        <div className="row-start-1 w-60">
          <div className="text-3xl">Username</div>
          <input type="text" className="w-full h-10 rounded-md"></input>
        </div>
        <div className="row-start-2 w-60">
          <div className="text-3xl">Password</div>
          <input type="text" className="w-full h-10 rounded-md"></input>
        </div>
        <div className="row-start-3 w-60">
          <div className="text-3xl">Confirm Password</div>
          <input type="text" className="w-full h-10 rounded-md"></input>
        </div>
      </div>
    </>
  );
};

export default Credentials;
