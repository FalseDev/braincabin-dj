interface ResponseData {
    success: boolean
    errors?: string[]
}

const acceptAnswer = async (button: HTMLButtonElement) => {
    const question_pk = +button.getAttribute('data-question')!
    const answer_pk = +button.getAttribute('data-answer')!

    const res = await fetch(`/forum/answer/accept/${question_pk}/${answer_pk}/`, {method:"POST"})

    const data = await res.json() as ResponseData

    if (data.success){
        const span = document.createElement('span')
        span.setAttribute('class','text-success')
        span.innerText = 'Accepted'
        button.replaceWith(span)
        const buttons = document.querySelectorAll('button.answer-accept')
        buttons.forEach(acceptAnswerButton=>acceptAnswerButton.remove())
        return null
    }

    data.errors?.forEach(err=>alert(err))
}
