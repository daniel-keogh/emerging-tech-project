new Vue({
    el: '#app',
    data() {
        return {
            result: '',
            query: '',
            error: {
                show: false,
                message: ''
            },
            invalidInput: false
        }
    },
    computed: {
        isInvalid() {
            return isNaN(+this.query);
        }
    },
    methods: {
        submit(e) {
            e.preventDefault();

            // Input validation
            if (!this.query || this.isInvalid)
                return;

            const options = {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    query: this.query
                }),
            };

            fetch("/api/speed", options)
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        this.result = res.data[0][0] + '';
                    } else {
                        throw new Error();
                    }

                    // Hide the error notification
                    if (this.error.show) {
                        this.error.show = false;
                    }
                })
                .catch(err => {
                    this.error = {
                        show: true,
                        message: err.message || 'Something bad happened'
                    }
                })
        }
    }
});
