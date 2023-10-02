import React, {useState} from 'react'
import { useNavigate } from 'react-router-dom'

import { preview } from '../assets'
import { getRandomPrompt } from '../utils'
import { FormField, Loader, DateTimePicker } from '../components'

const EventsScheduler = () => {
  const navigate = useNavigate()
  const [form, setForm] = useState({
    name: '',
    desc: '',
    date: '',
  })

  const [loading, setLoading] = useState(false)
  // const [selectedDate, setSelectedDate] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault()

    if(form.name) {
      setLoading(true)
      console.log(form)

      try {
        const response = await fetch('http://localhost:5000/schedule/event', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
          body: JSON.stringify(form),
        })

        await response.json()
        navigate('/')
      } catch (err) {
        console.log(form, err)
        alert(err)
      } finally {
        setLoading(false)
      }
    } else {
      alert('Please enter a prompt and Generate an image.')
    }
  }

  const handleChange = (e) => {
    console.log(e)
    if (e.target == undefined) {
      setForm({...form, ['date']: e})
    } else {
      setForm({...form, [e.target.name]: e.target.value })
    }
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
            name="desc"
            placeholder="description"
            value={form.desc}
            handleChange={handleChange}
          />
          <div>
            <DateTimePicker 
              labelName={"Schedule Date Time"} 
              handleChange={handleChange}
            />
          </div>
        </div>

        <div className='mt-6'>
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