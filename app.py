from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


# JOBS = [
#   {
#     'id' : 1,
#     'title' : 'Data Analyst',
#     'location' : 'Bengaluru, India',
#     'salary' : 'Rs. 15,00,000'
#   },
#   {
#     'id' : 2,
#     'title' : 'Data Scientist',
#     'location' : 'Hyderabad, India',
#     'salary' : 'Rs. 12,00,000'
#   },
#   {
#     'id' : 3,
#     'title' : 'Frontend Engineer',
#     'location' : 'Delhi, India',
#     'salary' : 'Rs. 18,00,000'
#   },
#   {
#     'id' : 4,
#     'title' : 'Backend Engineer',
#     'location' : 'San Francisco',
#     'salary' : '$120,000'
#   },
# ]



@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "NOT FOUND 404"
  return render_template("jobpage.html", job=job)

@app.route("/jobs/<id>/apply", methods=['post'])
def apply_to_job(id):
  # This is for get method
  # data = request.args
  # for post method
  data = request.form
  return jsonify(data)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
