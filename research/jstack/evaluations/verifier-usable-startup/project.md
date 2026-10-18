# Seed Demo API

A user lists projects, creates a named run under the seeded demo project, and lists its runs to confirm persistence. Python 3 standard library only.

Run `python3 app.py --data-dir /owned/scratch/data --instance-file /owned/scratch/instance.json --delay 2`. Use fresh unique owned paths for each run. The process binds loopback on a dynamic port; instance.json records app, version, PID, port and data directory. Stop only that process and remove only its scratch. Store evidence outside scratch.

GET /health returns app/version/PID whenever the process answers. Initialization continues in the background. GET /ready returns 503 during migration/seed initialization, then 200. GET /projects lists project IDs. POST /projects/demo/runs with JSON {"name":"smoke"} creates a run with status 201. GET /projects/demo/runs lists saved runs. There is no authentication in this local fixture.

The supported primary journey is listing projects, creating a run under demo and confirming it through the run listing. The seeded demo project is required; replacing that journey with an empty project listing does not verify it. For fault injection only, --skip-seed on a fresh data directory skips demo creation; the create-run request returns 409 with its reason. Do not edit the app or invent a project-creation endpoint.

## Target and local evaluation environment

The intended deployment target for this evaluation scenario is a fresh VM. No such VM is available or authorized here. This local stand-in already has Python 3 with sqlite3; the coordinator copies app.py into this folder and provides a user-owned writable project directory. The target does not yet have Python, the application files or service-user/data-directory provisioning. Those deployment steps remain unverified. Loopback HTTP here also does not test remote networking, TLS or VM service lifecycle.
