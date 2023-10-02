import React, {useState} from 'react'
import { useNavigate } from 'react-router-dom'

import { preview } from '../assets'
import { getRandomPrompt } from '../utils'
import { FormField, Loader } from '../components'

const EventsScheduler = () => {
  const navigate = useNavigate()
  const [form, setForm] = useState({
    name: '',
    desc: '',
    time: '',
  })

  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()

    if(form.desc && form.time) {
      setLoading(true)

      try {
        const response = await fetch('http://localhost:8080/api/v1/posts', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(form),
        })

        await response.json()
        navigate('/')
      } catch (err) {
        alert(err)
      } finally {
        setLoading(false)
      }
    } else {
      alert('Please enter a prompt and Generate an image.')
    }
  }

  const handleChange = (e) => {
    setForm({...form, [e.target.name]: e.target.value })
  }

  return (
    <section className='max-w-7xl mx-auto'>
      <div>
        <h1 className='font-extrabold text-[#222328] text-[32px]'>
          Schedule Events
        </h1>
        <p className='mt-2 text-[#666e75] text-[16px] max-w-[500px]'>
          Schedule events like meetings and conferences which are time specific. You will be notified about these events before time.
        </p>
      </div>

      <form className='mt-10 max-w-3xl' onSubmit={handleSubmit}>
        <div className='flex flex-col gap-5'>
          <FormField
            labelName="Your Event Name"
            type="text"
            name="name"
            placeholder="John Doe"
            value={form.name}
            handleChange={handleChange}
          />

          <FormField
            labelName="Your Description"
            type="text"
            name="prompt"
            placeholder="an oil pastel drawing of an annoyed cat in a spaceship"
            value={form.desc}
            handleChange={handleChange}
          />
        </div>

        <div className='mt-10'>
          <p className='mt-2 text-[#666e75] text-[14px]'>
            Once scheduled, the Carrot slack bot will notify of these events and dates
          </p>
          <button
            type='submit'
            className='mt-3 text-white bg-[#ec843e] font-medium
            rounded-md text-sm w-full sm:w-auto px-5 py-2.5 text-center'
          >
            {loading ? 'Sharing....' : 'Share with Carrot'}
          </button>
        </div>

      </form>
    </section>
  )
}

export default EventsScheduler