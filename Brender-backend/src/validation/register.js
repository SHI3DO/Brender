const Validator = require('validator');
const isEmpty = require('is-Empty');

module.exports = function validateRegisterInput(data) {
   let errors = {};

   data.name = !isEmpty(data.name) ? data.name : '';
   data.password = !isEmpty(data.password) ? data.password : '';
   data.computername = !isEmpty(data.computername) ? data.computername : '';

   if (Validator.isEmpty(data.name)) {
       errors.name = "Name field is required"
   }
   if (Validator.isEmpty(data.password)) {
       errors.password = "Password field is required"
   }
   if (Validator.isEmpty(data.computername)) {
       errors.computername = "Computername field is required"
   }

   return {
       errors,
       isValid: isEmpty(errors)
   }
};
