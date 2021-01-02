new Vue({
    el: '#app',
    data() {
        return {
            result: '',
            plot: '',
            models: [
                {
                    name: 'Linear',
                    key: 'lin'
                },
                {
                    name: 'Sigmoid',
                    key: 'sig'
                },
                {
                    name: 'Sigmoid (No Outliers)',
                    key: 'signo'
                },
            ],
            selectedModel: 'signo',
            query: '',
            error: {
                show: false,
                message: ''
            },
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
                    query: this.query,
                    model: this.selectedModel,
                }),
            };

            fetch('/api/speed', options)
                .then(res => res.json())
                .then(res => {
                    if (res.success) {
                        this.result = res.data.predictions[0] + '';
                        this.plot = res.data.plot;
                    } else {
                        throw new Error(res.message);
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
                });
        }
    }
});
