

node {
    stage('Build') {
        sh 'echo "Hello World"'
        sh '''
            echo "Multiline shell steps works too"
            ls -lah
        '''
    }
}

node {
    stage('Deploy') {
        retry(3) {
            sh './flakey-deploy.sh'
        }

        timeout(time: 3, unit: 'MINUTES') {
            sh './health-check.sh'
        }
    }
}

node {
    try {
        stage('Test') {
            sh 'echo "Fail!"; exit 1'
        }
        sh 'echo "This will run only if successful"'
    }
    catch (exc) {
        if (currentBuild.result == 'UNSTABLE') {
            sh 'echo "This will run only if the run was marked as unstable"'
        }
        if (currentBuild.result == 'FAILURE') {
            sh 'echo "This will run only if failed"'
        }
    }
    finally {
        sh 'echo "This will always run"'
    }
}
