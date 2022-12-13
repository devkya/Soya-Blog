import axios from 'axios';

const instance = axios.create({
	baseURL: 'http://localhost:8000/api/',
});

function getDetailPost() {
	instance
		.get()
		.then(res => {
			return res.data;
		})
		.catch(err => {
			return err;
		});
}

export { getTank3P };
