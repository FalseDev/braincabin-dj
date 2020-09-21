interface VoteResponseData {
    success: boolean
    errors?: string[]
}

interface IVoteOptions {
    action: string
    object: string
    voteType: string
    pk: number
}

// Make request url from the vote options 
const getUrl = (voteOptions: IVoteOptions) => `/forum/vote/${voteOptions.object}/${voteOptions.voteType}/${voteOptions.action}/${voteOptions.pk}/`


// Extract vote options from button data attributes
const getVoteOptions = (element: HTMLButtonElement): IVoteOptions => {
    const action = element.getAttribute('data-action') as string
    const object = element.getAttribute('data-object') as string
    const voteType = element.getAttribute('data-vote') as string
    const pk = +(element.getAttribute('data-pk') as string)

    return { action, object, voteType, pk }
}


const vote = async (clickedElement: HTMLButtonElement) => {

    const updateCountValues = (inverseButton: HTMLButtonElement) => {
        const counterElementID = clickedElement.getAttribute('data-counter')
        const counterElement = document.getElementById(counterElementID!) as HTMLSpanElement

        let count = +(counterElement?.innerText as string)
        voteOptions.action == 'add' ? count++ : count--

        counterElement.innerText = count.toString()

        if (inverseButton.getAttribute('data-action') == 'remove') {
            const inverseCounter = (document.getElementById(inverseButton.getAttribute('data-counter')!)!)
            const inverseCount = +inverseCounter.innerText
            inverseCounter.innerText = (inverseCount - 1).toString()
        }

        // Invert action data attribute
        clickedElement.setAttribute('data-action', voteOptions.action == 'add' ? 'remove' : 'add')
        inverseButton.setAttribute('data-action', 'add')
    }

    const updateArrowColors = (inverseButton: HTMLButtonElement) => {
        // Invert color 
        clickedElement.style.color = clickedElement.style.color == '' ? 'blue' : ''

        inverseButton.style.color = ''
    }

    const voteOptions = getVoteOptions(clickedElement)
    const url = getUrl(voteOptions)
    // Set options for request
    const options: RequestInit = { method: 'POST' }

    const res = await fetch(url, options)
    const resData: VoteResponseData = await res.json()

    if (resData.success) {
        const inverseButtonQuery = `[data-object="${voteOptions.object}"][data-pk="${voteOptions.pk}"][data-vote="${voteOptions.voteType == 'upvote' ? 'downvote' : 'upvote'}"]`
        const inverseButton = document.querySelector(inverseButtonQuery) as HTMLButtonElement
        updateCountValues(inverseButton)
        updateArrowColors(inverseButton)
    }

    else {
        alert(resData.errors![0])
    }
}

