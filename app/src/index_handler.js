var msgpack = require("msgpack-lite");
var playerJson = {};
var sessionToken = "";
/**
 * Cookie Manager
 */
 function setCookie(cname, cvalue, exhrs) {
     var d = new Date();
     d.setTime(d.getTime() + (exhrs * 60 * 60 * 1000));
     var expires = "expires="+d.toUTCString();
     document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
 }
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function checkCookie() {
    var user = getCookie("username");
    return user!="";
}


/**
 * Backend communication
 */
var update=function() {
    $.get("../getData/",sessionToken,function(data){handleUpdate(data)});
};

var handleUpdate=function(data) {
    playerJson = msgpack.decode(data);
};

var refresh_token=function() {
    if(checkCookie("userToken")){
        sessionToken = getCookie("userToken");
    } else {
        sessionToken = generate_token();
    }
    setCookie("userToken",sessionToken,24);
    $.post("/token",{sessionToken},connection_error);
};

var generate_token=function(username) {
    return Math.random().toString(36).substr(2)+Math.random().toString(36).substr(2);
};

var connection_error = function(){};

setInterval(update,100);
