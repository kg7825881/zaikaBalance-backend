 # cURL Examples for Zaika Balance Backend

## Sign Up
```bash
curl -X POST http://localhost:5000/auth/signup \
-H "Content-Type: application/json" \
-d '{"email":"user@example.com","password":"password123"}'

#login
curl -X POST http://localhost:5000/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"user@example.com","password":"password123"}'

#calculate BMI
curl -X POST http://localhost:5000/bmi/calculate \
-H "Content-Type: application/json" \
-d '{"height":170,"weight":65}'

#generate diet plan
curl -X POST http://localhost:5000/diet/generate \
-H "Content-Type: application/json" \
-d '{"bmi":22,"goal":"weight_loss"}'

#prdeict food
curl -X POST http://localhost:5000/food/predict \
-H "Content-Type: application/json" \
-d '{"ingredients":"rice, tomato, onion"}'

#log food for nutrient tracking
curl -X POST http://localhost:5000/tracker/log \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"foods":["apple","banana"]}'

#scan barcode image
curl -X POST http://localhost:5000/barcode/scan \
-H "Authorization: Bearer <token>" \
-F image=@/path/to/barcode.jpg

#submit feedback
curl -X POST http://localhost:5000/feedback/submit \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"feedback":"Great app!"}'



