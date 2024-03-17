import LoginIcon from '@mui/icons-material/Login';
import { Typography } from "@mui/material";
import Button from "@mui/material/Button";
import PropTypes from "prop-types";
import React, { Component } from "react";
export class LogIn extends Component {
  /**
   * Handles the click event of the sign in button an calls the prop onSignIn handler
   */
  constructor(props) {
    super(props);

    // Init the state
    this.state = {};
  }

  handleLogInButtonClicked = () => {
    this.props.onLogIn();
  };

  /** Renders the sign in page, if user objext is null */
  render() {
    const {} = this.props;
    return (
      <>
        <div style={{display:"flex", justifyContent:"center", alignItems:"center", flexDirection:"column", height: "70vh"}}>
          <Typography id="login_text">Bitte melde dich vor dem Benutzen der HeyDateMe-DatingApp mit deinem Google-Konto an.</Typography>
          <br>
          </br>
          <Button variant="contained" onClick={this.handleLogInButtonClicked} startIcon={<LoginIcon />}>
            &nbsp; Einloggen
          </Button>
        </div>
      </>
    );
  }
}

/** Component specific styles */

/** PropTypes */
LogIn.propTypes = {
  /** @ignore */
  classes: PropTypes.object,
  /**
   * Handler function, which is called if the user wants to sign in.
   */
  onLogIn: PropTypes.func,
};

export default LogIn;