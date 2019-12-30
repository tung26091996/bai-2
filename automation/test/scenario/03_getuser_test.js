Feature('Get Users');
const assert = require('assert');

Scenario('get user by email', async (I) => {
  let user = await I.sendGetRequest('/users/1');
  let user_email = user.data["email"];

  let result = await I.sendGetRequest('/users/' + user_email);

  assert.equal(user_email, result.data["email"]);

});