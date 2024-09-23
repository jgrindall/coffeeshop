import { Injectable } from '@angular/core';
import { JwtHelperService } from '@auth0/angular-jwt';
import { environment } from '../../environments/environment';

const JWTS_LOCAL_KEY = 'JWTS_LOCAL_KEY';

function parseJwt (token) {
    // https://stackoverflow.com/questions/38552003/how-to-decode-jwt-token-in-javascript
  var base64Url = token.split('.')[1];
  var base64 = decodeURIComponent(atob(base64Url).split('').map((c)=>{
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  return base64;
};


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url = environment.auth0.url;
  audience = environment.auth0.audience;
  clientId = environment.auth0.clientId;
  callbackURL = environment.auth0.callbackURL;
  loggedOutURL = environment.auth0.loggedOutURL;

  token: string;
  decodedToken: string;
  payload: any;

  constructor() { }

  build_logout_link() {
    let link = 'https://';
    link += this.url + '.auth0.com';
    link += '/v2/logout?';
    link += 'client_id=' + this.clientId + '&';
    link += 'returnTo=' + this.loggedOutURL;
    return link;
  }

  build_login_link(callbackPath = '') {
    let link = 'https://';
    link += this.url + '.auth0.com';
    link += '/authorize?';
    link += 'audience=' + this.audience + '&';
    link += 'response_type=token&';
    link += 'client_id=' + this.clientId + '&';
    link += 'redirect_uri=' + this.callbackURL + callbackPath;
    return link;
  }

  // invoked in app.component on load
  check_token_fragment() {
    // parse the fragment
    const fragment = window.location.hash.substr(1).split('&')[0].split('=');
    // check if the fragment includes the access token
    if ( fragment[0] === 'access_token' ) {
      // add the access token to the jwt
      this.token = fragment[1];
      this.decodedToken = parseJwt(this.token);
      // save jwts to localstore
      this.set_jwt();
    }
  }

  set_jwt() {
    localStorage.setItem(JWTS_LOCAL_KEY, this.token);
    if (this.token) {
      this.decodeJWT(this.token);
    }
  }

  load_jwts() {
    this.token = localStorage.getItem(JWTS_LOCAL_KEY) || null;
    if (this.token) {
      this.decodeJWT(this.token);
      this.decodedToken = parseJwt(this.token);
    }
  }

  activeJWT() {
    return this.token;
  }

  decodeJWT(token: string) {
    const jwtservice = new JwtHelperService();
    this.payload = jwtservice.decodeToken(token);
    return this.payload;
  }

  logout() {
      this.token = '';
      this.decodedToken = '';
      this.payload = null;
      this.set_jwt();
      setTimeout(() => {
        window.location.href = this.build_logout_link();
      })

      
  }

  can(permission: string) {
    console.log("checking permission", permission, this.payload, this.payload ? this.payload.permissions : []);
    return this.payload && this.payload.permissions && this.payload.permissions.length && this.payload.permissions.includes(permission);
  }
}
