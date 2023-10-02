import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

const DateTimePicker = ({ labelName, handleChange }) => {
  const [selectedDate, setSelectedDate] = useState(null);

  return (
    <div>
        <div className='flex items-center gap-2 mb-2'>
        <label 
            htmlFor='date'
            className='block text-sm font-medium text-gray-900'
        >
          {labelName}
        </label>
        </div>
        <DatePicker
            id={"date"}
            name={"date"}
            selected={selectedDate}
            onChange={(date) => {
                handleChange(date)
                setSelectedDate(date)
            }}
            showTimeSelect
            timeFormat="HH:mm"
            timeIntervals={15}
            timeCaption="Time"
            dateFormat="MMMM d, yyyy h:mm aa"
            className="px-4 py-2 border rounded-md focus:outline-none focus:ring focus:border-blue-300"
        />
    </div>
  );
};

export default DateTimePicker;
