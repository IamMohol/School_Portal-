<template>
    <div id="finance">
        <v-container app>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-card-text>
                            <v-icon>trending_up</v-icon>
                            <div class="headline">Finance</div>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-breadcrumbs :items="breadcrumb" divider=">"/>
                    </v-card>
                </v-flex>
            </v-layout>

            <v-layout row pb-2>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-card-text>
                            <div class="headline">Current Semester Fee Status</div>
                        </v-card-text>
                        <v-simple-table>
                            <thead>
                            <tr>
                                <th>Current Invoice</th>
                                <th>Amount Paid</th>
                                <th>Balance</th>
                            </tr>

                            </thead>
                            <tbody>
                            <tr v-for="t in finance">
                                <td><v-chip  color="#f05d5e" dark>-{{t.invoice}}</v-chip></td>
                                <td><v-chip  color="#d7fff1 dark">+{{t.fee_paid}}</v-chip></td>
                                <td><v-chip  color="#3b60e4">{{x=t.fee_paid - t.invoice}}</v-chip></td>
                            </tr>

                            </tbody>
                        </v-simple-table>
                    </v-card>
                </v-flex>
            </v-layout>

            <v-layout row>
                <v-flex xs12 md12>
                    <v-card flat>
                        <v-card-title>Finance History
                            <v-spacer></v-spacer>
                            <v-text-field v-model="search" append-icon="search" label="Search" single-line
                                          hide-details></v-text-field>
                        </v-card-title>

                        <v-data-table
                                :headers="headers"
                                :items="financeHistory"
                                :search="search"></v-data-table>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>
<script>
    export default {
        name: "Finance",
        data() {
            return {
                finance: null,
                breadcrumb: [
                    {
                        text: 'Home',
                        disabled: false,
                        href: '/#/',
                    },
                    {
                        text: 'Finance',
                        disabled: true,
                        href: '/#/Finance',
                    },
                ],
                search: '',
                headers: [
                    {
                        text: 'Amount (Kshs)',
                        align: 'left',
                        sortable: true,
                        value: 'amount',
                    },
                    {text: 'Date Posted', value: 'date_posted'},
                    {text: 'Description', value: 'description'},
                    // {text: 'id', value: 'id'},
                    // {text: 'student', value: 'student'},
                    {text: 'Transaction ID', value: 'trx_id'},
                    {text: 'Type', value: 'type'},

                ],

                financeHistory: [],
            }
        },
        methods: {
            getFinance() {
                var p = this;
                axios
                    .get('/finance/current/')
                    .then(response => (
                        p.finance = response.data
                    ))
                    .catch(error => (console.log(error)))
            },
            getFinanceHistory() {
                var p = this;
                axios
                    .get('/finance/history/')
                    .then(response => (
                        p.financeHistory = response.data
                    ))
                    .catch(error => (console.log(error)))
            }
        },
        created() {
            this.getFinance();
            this.getFinanceHistory();
        }
    }
</script>
<style></style>