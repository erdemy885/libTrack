const Credentials = () => {
  return (
    <>
      <div className="px-16 pt-11 bg-amber-700 rounded-3xl grid grid-rows-4 row-start-4 place-items-center space-y-5">
        <div className="w-80">
          <div className="text-3xl">Username</div>
          <input type="text" className="w-full"></input>
        </div>
        <div className="w-80">
          <div className="text-3xl">Password</div>
          <input type="text" className="w-full"></input>
        </div>
        <div className="w-80">
          <div className="text-3xl">Confirm Password</div>
          <input type="text" className="w-full"></input>
        </div>
      </div>
    </>
  );
};

export default Credentials;
