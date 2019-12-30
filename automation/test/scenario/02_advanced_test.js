
Feature('Advanced Operations');
const assert = require('assert');


Scenario('change password success', async (I) => {
  let user = await I.sendGetRequest('/users/1');
  let user_email = user.data["email"];

  let result = await I.sendPostRequest('/users/change_pass',
    { 'email': user_email, 'pass': 'new_pa$$w@rd123' }
  );
  assert.equal(result.data['status'], true);

});


Scenario('password is too short', async (I) => {
  let user = await I.sendGetRequest('/users/2');
  let user_email = user.data["email"];

  let result = await I.sendPostRequest('/users/change_pass',
    { 'email': user_email, 'pass': 'abc12' }
  );
  assert.equal(result.data['status'], false);

});

Scenario('password does not contain numeric', async (I) => {
  let user = await I.sendGetRequest('/users/2');
  let user_email = user.data["email"];

  let result = await I.sendPostRequest('/users/change_pass',
    { 'email': user_email, 'pass': 'abcdefghijklm' }
  );
  assert.equal(result.data['status'], false);

});