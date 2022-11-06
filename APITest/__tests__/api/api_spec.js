const frisby = require('frisby');

const Joi = frisby.Joi;

it('should return status 200', function () 
{
   return frisby.get('http://localhost:3000/')
     .expect("status", 200)
});