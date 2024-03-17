export default class API {
  // Singelton instance
  static #api = null;
  #OneServerBaseURL = "/HeyDateMe";

  // Vervollständigt die Url mit dem Prefix und Suffix
  #setUrl = (suffix) => `${this.#OneServerBaseURL}/${suffix}`;
  static getAPI() {
    if (this.#api == null) {
      this.#api = new API();
    }
    return this.#api;
  }
  #fetchAdvanced = (url, init) =>
    fetch(url, { credentials: "include", ...init }).then((res) => {
      if (!res.ok) {
        throw Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    });

  get(url, bo) {
    return this.#fetchAdvanced(this.#setUrl(url)).then((responseJSON) => {
      let response = bo.fromJSON(responseJSON);
      return new Promise(function (resolve) {
        resolve(response);
      });
    });
  }
  create(url, object, bo) {
    return this.#fetchAdvanced(this.#setUrl(url), {
      method: "POST",
      headers: {
        Accept: "application/json, text/plain",
        "Content-type": "application/json",
      },
      body: JSON.stringify(object),
    }).then((responseJSON) => {
      let response = bo.fromJSON(responseJSON)[0];
      return new Promise(function (resolve) {
        resolve(response);
      });
    });
  }
  update(url, object, bo) {
    return this.#fetchAdvanced(this.#setUrl(url), {
      method: "PUT",
      headers: {
        Accept: "application/json, text/plain",
        "Content-type": "application/json",
      },
      body: JSON.stringify(object),
    }).then((responseJSON) => {
      // We always get an array of UserBO.fromJSON
      let response = bo.fromJSON(responseJSON)[0];
      //
      return new Promise(function (resolve) {
        resolve(response);
      });
    });
  }

  delete(url, bo) {
    return this.#fetchAdvanced(this.#setUrl(url), {
      method: "DELETE",
    }).then((responseJSON) => {
      // We always get an array of UserBO.fromJSON
      let response = bo.fromJSON(responseJSON)[0];
      return new Promise(function (resolve) {
        resolve(response);
      });
    });
  }
}
