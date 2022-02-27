import React, { useState, useEffect } from "react";
import axios from "axios";
import Login from "./auth/login";

const Home = (props) => {
  const [state, setState] = useState("");

  useEffect(() => {
    axios
      .post("http://localhost:5000/auth/login", {
        email: "famousss@gmail.com",
        password: "1234",
      })
      .then((res) => setState(res.data.Authorization));
  }, []);

  return (
    <div>
      <Login></Login>
      <p>{state}</p>
    </div>
  );
};

export default Home;
