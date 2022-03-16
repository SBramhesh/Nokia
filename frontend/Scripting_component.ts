import React, {useEffect, ReactElement, Component} from "react"
import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib"
import * as Yup from 'yup'
import {Formik, Form, Field} from 'formik'

import Card from '@material-ui/core/Card'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import Typography from '@material-ui/core/Typography'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'


function ScriptingComponent({args}: ComponentProps): ReactElement {
  const {title} = args

  

  useEffect(() => {
    Streamlit.setFrameHeight()
  })

  const onSubmit = (values: any, {setSubmitting}: any) => {
    setSubmitting(false)
    Streamlit.setComponentValue('values')
  }

  const onReset = () => Streamlit.setComponentValue({})

  return "This is the Scripting component" as unknown as ReactElement
}

export default withStreamlitConnection(ScriptingComponent)