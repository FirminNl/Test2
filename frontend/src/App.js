import { initializeApp } from "firebase/app";
import {
  getAuth,
  GoogleAuthProvider,
  onAuthStateChanged,
  signInWithPopup,
} from "firebase/auth";
import React from "react";
import { Navigate } from "react-router";
import {
  Route,
  BrowserRouter as Router,
  Routes,
  useLocation,
} from "react-router-dom";
import UserProfileView from "./api/Views/UserProfileView";
import "./App.css";
import NavBar from "./componnents/NavBar";
import firebaseConfig from "./firebaseconfig";
import Anfragen from "./pages/Anfragen";
import Blockiert from "./pages/Blockiert";
import Chats from "./pages/Chats";
import LogIn from "./pages/Login";
import Matching from "./pages/Matching";
import Merkliste from "./pages/Merkliste";
import Profil from "./pages/Profil";

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
class App extends React.Component {
  /** Constructor of the app, which initializes firebase  */
  constructor(props) {
    super(props);

    // Init an empty state
    this.state = {
      currentUser: null,
      appError: null,
      authError: null,
      authLoading: false,
      user: null,
      isSaved: false,
      fnSaved: false,
    };
  }

  /**
   * Create an error boundary for this app and recieve all errors from below the component tree.
   *
   * @See See Reacts [Error Boundaries](https://reactjs.org/docs/error-boundaries.html)
   */
  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { appError: error };
  }

  /**
   * Handles the sign in request of the SignIn component uses the firebase.auth() component to sign in.
   * @see See Google [firebase.auth()](https://firebase.google.com/docs/reference/js/firebase.auth.Auth)
   * @see See Google [firebase.auth().signInWithRedirect](https://firebase.google.com/docs/reference/js/firebase.auth.Auth#signinwithredirect)
   */
  handleSignIn = () => {
    this.setState({
      authLoading: true,
    });

    const provider = new GoogleAuthProvider();

    auth.languageCode = "en";
    signInWithPopup(auth, provider);
  };

  getUserByGuid = (currentUser) => {
    UserProfileView.getView()
      .getByGuid(currentUser.uid)
      .then((prof) => {
        this.setState({
          success: true,
          successMessage: `${prof[0].getFirstname()} | ID=${prof[0].getID()} mit der GUID ${prof[0].getGoogleUserId()}`,
          error: false,
          user: prof[0],
        });
      })
      .catch((err) => console.log("error", err));
  };
  /**
   * Lifecycle method, which is called when the component gets inserted into the browsers DOM.
   * Initializes the firebase SDK.
   *
   * @see See Googles [firebase init process](https://firebase.google.com/docs/web/setup)
   */

  componentDidMount() {
    auth.languageCode = "en";
    onAuthStateChanged(auth, (user) => {
      if (user) {
        this.setState({
          authLoading: true,
        });
        // The user is signed in
        user
          .getIdToken()
          .then((token) => {
            // Add the token to the browser's cookies. The server will then be
            // able to verify the token against the API.
            // SECURITY NOTE: As cookies can easily be modified, only put the
            // token (which is verified server-side) in a cookie; do not add other
            // user information.
            document.cookie = `token=${token};path=/`;
            // console.log("Token is: " + document.cookie);

            // Set the user not before the token arrived
            this.setState({
              currentUser: user,
              authError: null,
              authLoading: false,
            });
            this.getUserByGuid(user);
          })
          .catch((e) => {
            this.setState({
              authError: e,
              authLoading: false,
            });
          });
      } else {
        // User has logged out, so clear the id token
        document.cookie = "token=;path=/";

        // Set the logged out user to null
        this.setState({
          currentUser: null,
          authLoading: false,
        });
      }
    });
  }

  handleIsSaved = (isSaved) => {
    this.setState({
      isSaved: isSaved,
    });
  };
  handleFirstnameSaved = (fnSaved) => {
    this.setState({
      fnSaved: fnSaved,
    });
  };

  /** Renders the whole app */
  render() {
    const { currentUser, user } = this.state;
    return (
      <>
        <Router>
          <NavBar
            user={user}
            isSavedProp={this.state.isSaved}
            fnSaved={this.state.fnSaved}
          />
          <Routes>
            <Route>
              <Route
                path={process.env.PUBLIC_URL + "/"}
                element={
                  currentUser ? (
                    <Navigate replace to={process.env.PUBLIC_URL + "/Profil"} />
                  ) : (
                    <LogIn onLogIn={this.handleSignIn} />
                  )
                }
              />
              <Route
                path="/Profil"
                onLeave={this.showConfirm}
                element={
                  <Secured user={currentUser}>
                    {user ? (
                      <Profil
                        user={user}
                        handleIsSaved={this.handleIsSaved}
                        handleFirstnameSaved={this.handleFirstnameSaved}
                      />
                    ) : null}
                  </Secured>
                }
              />
              <Route
                path="/Matching"
                element={
                  <Secured user={currentUser}>
                    <Matching user={user} />
                  </Secured>
                }
              />
              <Route
                path="/Anfragen"
                element={
                  <Secured user={currentUser}>
                    <Anfragen user={user} />
                  </Secured>
                }
              />
              <Route
                path="/Chats"
                element={
                  <Secured user={currentUser}>
                    <Chats user={user} />
                  </Secured>
                }
              />
              <Route
                path="/Blockiert"
                element={
                  <Secured user={currentUser}>
                    <Blockiert user={user} />
                  </Secured>
                }
              />
              <Route
                path="/Merkliste"
                element={
                  <Secured user={currentUser}>
                    <Merkliste user={user} />
                  </Secured>
                }
              />
            </Route>
          </Routes>
        </Router>
      </>
    );
  }
}

export default App;

function Secured(props) {
  let location = useLocation();

  if (!props.user) {
    // Redirect them to the /login page, but save the current location they were
    // trying to go to when they were redirected. This allows us to send them
    // along to that page after they login, which is a nicer user experience
    // than dropping them off on the home page.
    return (
      <Navigate
        to={process.env.PUBLIC_URL + "/"}
        state={{ from: location }}
        replace
      />
    );
  }

  return props.children;
}
